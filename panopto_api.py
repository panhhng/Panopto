from zeep import Client

def get_client(servername):
    return Client(f"https://{servername}/Panopto/PublicAPI/4.6/UserManagement.svc?wsdl")

def get_array_type(client):
    return client.get_type('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}ArrayOfguid')

def delete_users(client, AuthenticationInfo, merged_df, preview_callback=None):
    if merged_df is None or merged_df.empty:
        raise ValueError("No merged users to delete.")

    user_ids = merged_df['User ID'].dropna().astype(str).tolist()
    emails = merged_df['Email'].dropna().tolist()

    if not user_ids:
        raise ValueError("No valid UserIDs found.")

    if preview_callback:
        proceed = preview_callback(emails)
        if not proceed:
            return 0 

    array_type = get_array_type(client)
    guid_list = array_type(guid=user_ids)
    client.service.DeleteUsers(auth=AuthenticationInfo, userIds=guid_list)

    return len(user_ids)
