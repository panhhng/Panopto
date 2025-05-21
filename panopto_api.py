from zeep import Client

def get_client(servername):
    return Client(f"https://{servername}/Panopto/PublicAPI/4.6/UserManagement.svc?wsdl")

def get_array_type(client):
    return client.get_type('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}ArrayOfguid')

def delete_users(client, AuthenticationInfo, merged_df):
    if merged_df is None or merged_df.empty:
        raise ValueError("No merged users to delete.")

    user_ids = merged_df['UserID'].dropna().astype(str).tolist()

    if not user_ids:
        raise ValueError("No valid UserIDs found.")

    array_type = get_array_type(client)
    guid_list = array_type(guid=user_ids)
    client.service.DeleteUsers(auth=AuthenticationInfo, userIds=guid_list)

    return len(user_ids)
