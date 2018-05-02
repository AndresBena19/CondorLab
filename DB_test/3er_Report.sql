SELECT COUNT(R.cd_role_type) as Non_active_Providers
FROM user_role R
WHERE R.cd_role_type = "Provider" AND R.in_status = 0