
SELECT RR.cd_role_type as User_Type, COUNT(RR.in_status) as Total_Active,
(
SELECT COUNT(R.cd_role_type)
FROM user_profile P
INNER JOIN user_role R
ON
P.id_user = R.id_user 
WHERE P.nm_middle IS NULL AND R.cd_role_type = RR.cd_role_type
) as No_Middle_Name
FROM user_role RR
GROUP BY RR.cd_role_type, RR.in_status
HAVING RR.in_status = 1 




