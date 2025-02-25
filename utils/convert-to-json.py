import csv
import json
import sys
import codecs
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

# Constants
ABOUT_TITLE = "Digital Innovation Curated VR Apps"
DATE_FORMAT = "%d %b %Y"
REQUIRED_COLUMNS = ['name', 'title', 'url', 'about']

def get_column_indices(headers: List[str]) -> Dict[str, int]:
    """
    Get indices of required columns from headers.
    
    Args:
        headers (List[str]): List of CSV headers
        
    Returns:
        Dict[str, int]: Dictionary mapping required column names to their indices
    """
    # Convert headers to lowercase for case-insensitive matching
    header_map = {h.lower().strip(): i for i, h in enumerate(headers)}
    
    # Get indices for required columns
    column_indices = {}
    for required_col in REQUIRED_COLUMNS:
        if required_col in header_map:
            column_indices[required_col] = header_map[required_col]
        else:
            print(f"Error: Required column '{required_col}' not found in CSV.")
            sys.exit(1)
            
    return column_indices

def read_csv_file(file_path: str) -> Tuple[List[str], List[List[str]]]:
    """
    Read CSV file with UTF-8 encoding.
    
    Args:
        file_path (str): Path to CSV file
        
    Returns:
        Tuple[List[str], List[List[str]]]: Headers and data rows
    """
    try:
        with codecs.open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            headers = next(reader, None)  # Get headers
            if not headers:
                print("Error: CSV file is empty")
                sys.exit(1)
            
            # Clean headers
            headers = [h.strip() for h in headers]
            
            # Read and clean data rows
            rows = [[field.strip() for field in row] for row in reader]
            
            return headers, rows
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except UnicodeError as e:
        print(f"Error: Encoding issue in '{file_path}': {str(e)}")
        print("Please ensure the file is properly encoded in UTF-8.")
        sys.exit(1)

def process_bookmark_rows(rows: List[List[str]], column_indices: Dict[str, int]) -> List[Dict[str, Any]]:
    """
    Process CSV rows into JSON group structure.
    
    Args:
        rows (List[List[str]]): CSV rows (excluding header)
        column_indices (Dict[str, int]): Mapping of required columns to their indices
        
    Returns:
        List[Dict[str, Any]]: List of group dictionaries
    """
    groups = []
    current_group: Optional[Dict[str, Any]] = None
    
    for row in rows:
        # Extend row if it's shorter than maximum column index
        while len(row) <= max(column_indices.values()):
            row.append("")
            
        # Extract values using column indices
        name = row[column_indices['name']]
        title = row[column_indices['title']]
        url = row[column_indices['url']]
        about = row[column_indices['about']]
        
        # If there's a name, this is a new group
        if name:
            if current_group:
                groups.append(current_group)
            current_group = {
                "name": name,
                "bookmarks": []
            }
        # If no name but we have other fields, this is a bookmark entry
        elif current_group is not None and (title or url or about):
            bookmark = {
                "title": title,
                "url": url,
                "about": about
            }
            current_group["bookmarks"].append(bookmark)
    
    # Don't forget to add the last group
    if current_group:
        groups.append(current_group)
    
    return groups

def create_json_structure(groups: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Create final JSON structure with about section and groups.
    
    Args:
        groups (List[Dict[str, Any]]): List of processed groups
        
    Returns:
        Dict[str, Any]: Final JSON structure
    """
    return {
        "about": {
            "title": ABOUT_TITLE,
            "created": datetime.now().strftime(DATE_FORMAT)
        },
        "groups": groups
    }

def write_json_file(data: Dict[str, Any], output_path: str) -> None:
    """
    Write JSON data to file with UTF-8 encoding and pretty printing.
    
    Args:
        data (Dict[str, Any]): JSON data to write
        output_path (str): Path for output JSON file
    """
    try:
        with codecs.open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Error writing to '{output_path}': {str(e)}")
        sys.exit(1)
    except UnicodeError as e:
        print(f"Error: Encoding issue while writing '{output_path}': {str(e)}")
        sys.exit(1)

def convert_bookmarks(input_path: str, output_path: str) -> None:
    """
    Convert bookmark CSV file to JSON file.
    
    Args:
        input_path (str): Path to input CSV file
        output_path (str): Path for output JSON file
    """
    # Read CSV file
    headers, rows = read_csv_file(input_path)
    
    # Get column indices for required columns
    column_indices = get_column_indices(headers)
    
    # Optional: Print information about additional columns
    all_columns = set(headers)
    required_columns = set(REQUIRED_COLUMNS)
    extra_columns = all_columns - required_columns
    if extra_columns:
        print("\nInfo: Following additional columns will be ignored:")
        for col in sorted(extra_columns):
            print(f"- {col}")
        print()
    
    # Process rows
    groups = process_bookmark_rows(rows, column_indices)
    
    # Create final JSON structure
    json_data = create_json_structure(groups)
    
    # Write to JSON file
    write_json_file(json_data, output_path)
    
    print(f"Successfully converted '{input_path}' to '{output_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("No command-line arguments provided.")
        user_response = input("Do you want to convert 'bookmarks.csv' to 'bookmarks.json'? (yes/no): ").strip().lower()
        
        if user_response in ("yes", "y"):
            input_path = "bookmarks.csv"
            output_path = "bookmarks.json"
        else:
            print("Usage: python script.py input.csv output.json")
            sys.exit(1)
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
    
    convert_bookmarks(input_path, output_path)
