SELECT COUNT(R.cd_role_type) as Active_Licensees_With_Address_Info
FROM user_role R
WHERE R.cd_role_type IN ("Licensee","limited") AND R.in_status = 1