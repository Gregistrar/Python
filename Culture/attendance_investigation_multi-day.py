import sqlalchemy
import pandas as pd

conn_mssql = sqlalchemy.create_engine(MySQL Connection)
conn_mssql.connect()
assignment_date = '2018-06-14'

conn_pgsql = sqlalchemy.create_engine(PostgreSQL Connection)
conn_pgsql.connect()

days_of_week = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday'
}


# Gather the number of Fridays/Days a scholar has unexcused absences
friday_abs = '''
WITH attendance AS (
SELECT 
        scholar_id
        , class_infractions.date::date
--        , EXTRACT(DAY FROM class_infractions.date)
        , EXTRACT(DOW FROM class_infractions.date) AS dow

FROM absence
INNER JOIN class_infractions ON absence.class_infractions_id = class_infractions.id
WHERE class_infractions.date BETWEEN ('2017-08-14'::date) and ('2018-06-14'::date)
AND excused = False
AND class_infractions.is_in_session = true
)

SELECT *
FROM attendance
WHERE dow = '{day}'

'''

absence_frames = {}
for day in range(1, 6):
    print("Processing......", days_of_week.get(day))
    day_absent = pd.read_sql(friday_abs.format(day=day), conn_pgsql)
    current_day = days_of_week.get(day)+" absences"
    day_absent.rename(columns={'dow': current_day}, inplace=True)
    absence_frames[days_of_week.get(day)+" absences"] = day_absent

concat_absences = pd.concat(absence_frames, ignore_index=True)
concat_absences.set_index('scholar_id')
count_absences = concat_absences.groupby(['scholar_id']).count()

count_absences.info()
count_absences.head()

# Gather # of Fridays a scholar has unexcused tardies
friday_tardy = '''
WITH tardies AS (
SELECT 
        scholar_id
        , class_infractions.date::date
--        , EXTRACT(DAY FROM class_infractions.date)
        , EXTRACT(DOW FROM class_infractions.date) AS dow

FROM tardy
INNER JOIN class_infractions ON tardy.class_infractions_id = class_infractions.id
WHERE class_infractions.date BETWEEN ('2017-08-14'::date) and ('2018-06-14'::date)
AND excused = False
AND class_infractions.is_in_session = true
)

SELECT *
FROM tardies
WHERE dow = '{day}'

'''

tardy_frames = {}
for day in range(1, 6):
    print("Processing......", days_of_week.get(day))
    day_tardy = pd.read_sql(friday_tardy.format(day=day), conn_pgsql)
    current_day = days_of_week.get(day)+" tardies"
    day_tardy.rename(columns={'dow': current_day}, inplace=True)
    tardy_frames[days_of_week.get(day)+" tardies"] = day_tardy

concat_tardies = pd.concat(tardy_frames, ignore_index=True)
concat_tardies.set_index('scholar_id')
count_tardies = concat_tardies.groupby(['scholar_id']).count()

count_tardies.info()
count_tardies.head()

# Gather total # of Fridays in attendance\

total_fridays = '''
WITH target_date AS (
    SELECT s.id AS scholar_id
    , s.enrollment_date
    , generate_series(
        (CASE WHEN s.enrollment_date > '2017-08-14' THEN s.enrollment_date
            ELSE '2017-08-14' END)::date
        , (CASE WHEN s.Exit_Date < '2018-06-14' THEN s.Exit_Date
            ELSE '2018-06-14' END)::date
        , '1 day')::date AS date_range

    FROM scholar AS s
    WHERE (s.status = 1 
        OR s.Exit_Date >= '2018-06-06')
        AND s.withdrawn_without_attending = false
    )

SELECT scholar_id
    , date_range
    , EXTRACT(DOW FROM date_range) AS dow
FROM target_date
'''

friday_days = pd.read_sql(total_fridays.format(assignment_date=assignment_date), conn_pgsql)
friday_days.head(10)
friday_days.info()

dates_to_remove = ['2017-09-04', '2017-09-05', '2017-10-09', '2017-10-10', '2017-10-11',
                   '2017-11-20', '2017-11-21', '2017-11-22', '2017-11-23', '2017-11-24',
                   '2017-12-22', '2017-12-25', '2017-12-26', '2017-12-27', '2017-12-28',
                   '2017-12-29', '2018-01-01', '2018-01-02', '2018-01-03', '2018-01-15',
                   '2018-01-16', '2018-02-19', '2018-02-20', '2018-03-05', '2018-03-06',
                   '2018-03-07', '2018-03-08', '2018-03-09', '2018-03-12', '2018-04-16',
                   '2018-05-04', '2018-05-07', '2018-05-28']
friday_days['date_range'] = pd.to_datetime(friday_days['date_range'])
all_days = friday_days[~friday_days['date_range'].isin(dates_to_remove)]

day_frames = {}
for day in range(1,6):
    print("Processing......", days_of_week.get(day))
    copy_target = all_days.copy()
    current_day = days_of_week.get(day) + " total days"
    copy_target.rename(columns={'dow': current_day}, inplace=True)
    day_frames[days_of_week.get(day) + " total days"] = copy_target.loc[copy_target[current_day] == day]

concat_days = pd.concat(day_frames, ignore_index=True)
concat_days.set_index('scholar_id')
count_days = concat_days.groupby(['scholar_id']).count()
count_days.head()


# Pull active scholars from SMS
scholars_sms = '''
SELECT
        s.ID AS scholar_id
        , p.FirstName AS first_name
        , p.LastName AS last_name
        , sch.Name AS school_name
        , sch.Abbreviation AS school_abbr
        , p5.FirstName AS sm_first
        , p5.LastName AS sm_last
        --, s.CurrentGrade as grade
        , sc.Grade AS grade
        , sc.Nickname AS homeroom
        --, sc.nickname AS "ELA Class"
        , sc.homeroomtype
        --, sc.AcademicYearID
        --, CASE WHEN sc.homeroomtype = 1 THEN 'General'
        --    WHEN sc.homeroomtype = 2 THEN 'CTT'
        --    WHEN sc.homeroomtype = 3 THEN 'TwelveOneOne' END AS "Homeroom Type"
        --, CASE WHEN sch.schooltype = 1 THEN 'Elementary'
        --    WHEN sch.schooltype = 2 THEN 'Middle'
        --    WHEN sch.schooltype = 3 THEN 'High'
        --    WHEN sch.schooltype = 4 THEN 'Other' END AS "School Type"
        , s.cityrefno AS osis
        , s.entryschoolid
        , s.enrollmentdate
        , p.birthdate
        , p.gender
        , s.isell
        --, p.Email AS scholar_email
        --, p2.FirstName AS SL_first
        --, p2.LastName AS SL_last
        --, p2.Email AS SL_email
        , p3.FirstName AS teacher_first
        , p3.LastName AS teacher_last
        , p4.FirstName AS colead_teacher_first
        , p4.LastName AS colead_teacher_last
        --, s.studentno
        , s.exitdate


FROM Scholar s
INNER JOIN ClassEnrollment ce
    ON ce.ScholarID = s.ID
    AND ('{assignment_date}' BETWEEN ce.EffectiveDate AND ce.TerminationDate)
--    AND ('{assignment_date}' >= ce.EffectiveDate AND ('{assignment_date}' <= ce.TerminationDate OR ce.TerminationDate IS NULL))  
INNER JOIN Person p
        ON s.ID = p.ID
LEFT JOIN SchoolClass sc
    ON ce.HomeroomID = sc.ID
LEFT JOIN School AS sch
        ON sc.SchoolID = sch.ID
LEFT JOIN Person p2
    ON sch.LeaderStaffID = p2.ID
LEFT JOIN Person p3
    ON p3.ID = sc.TeacherStaffID
LEFT JOIN Person p4
    ON p4.ID = sc.CoLeadTeacherStaffID
LEFT JOIN Person p5
    ON p5.ID = sch.MDStaffID


WHERE
    s.CurrentGrade IN (0,1,2,3,4,5,6,7,8,9,10,11,12)
--    sc.Grade IN (5,6,7,8)
    AND (s.Status = 1 OR s.ExitDate >= '2018-06-14')
    AND sch.Abbreviation NOT LIKE 'XX-%'
    AND sc.subjectID IS NULL
--    AND sc.AcademicYearID = 397
    AND sc.HomeRoomType IS NOT NULL
--    AND sc.subjectID IN (6, 10028, 10029, 10030, 1)
--    AND sc.homeroomtype = 2
--    AND ca.subjectid IS NULL
    AND s.withdrawnwithoutattending = 'false'
    

ORDER BY s.ID
'''

scholar = pd.read_sql(scholars_sms.format(assignment_date=assignment_date), conn_mssql)
scholar['grade'] = scholar['grade'].map(
    {0: 'K', 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12})
scholar['school_name'] = scholar['school_name'].str.replace('Success Academy ', '')
# scholar['school'] = scholar['school'].str.replace('SA-', '')

scholar.head()
scholar.info()
#scholar.groupby(['school'])['school'].count().to_clipboard()
#scholar.groupby(['school'])['grade'].count().to_clipboard()
scholar = scholar.drop_duplicates()

fridays = pd.merge(scholar, count_days, how='left', on='scholar_id')
fridays_with_absence = pd.merge(fridays, count_absences, how='left', on='scholar_id')
fridays_final = pd.merge(fridays_with_absence, count_tardies, how='left', on='scholar_id')
fridays_final.head()
fridays_final.info()


fridays_final.to_csv('~/desktop/all_days_culture_6.14.18.csv', encoding='utf-8')

fridays_final.to_csv('~/desktop/scholar_friday_culture_6.14.18.csv', encoding='utf-8')
fridays_final.to_csv('~/desktop/last_two_fridays_6.14.18.csv', encoding='utf-8')
