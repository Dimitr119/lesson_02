from job1.dal import local_disk, sales_api


def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    json_content = sales_api.get_sales(date = date)
    local_disk.save_to_disk(json_content = json_content, path = raw_dir)