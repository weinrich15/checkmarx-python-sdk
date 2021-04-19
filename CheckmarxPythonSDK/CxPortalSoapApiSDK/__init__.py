from .CxPortalWebService import (
    add_license_expiration_notification,
    create_new_preset,
    create_scan_report,
    delete_preset,
    export_preset,
    export_queries,
    get_path_comments_history,
    get_queries_categories,
    get_query_collection,
    get_query_id_by_language_group_and_query_name,
    get_name_of_user_who_marked_false_positive_from_comments_history,
    get_preset_list,
    get_server_license_data,
    get_server_license_summary,
    delete_project,
    delete_projects,
    get_version_number,
)

from .CxAuditWebService import (
    get_files_extensions,
    get_source_code_for_scan,
)
