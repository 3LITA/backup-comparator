import gzip
import json
import os

from pathlib import Path


def compare_backups(source_path: str, target_path: str, backup_path: str) -> None:

    src_files = list()
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(".gz"):
                src_files.append(Path(os.path.join(root, file)))

    tgt_files = list()
    for root, dirs, files in os.walk(target_path):
        for file in files:
            if file.endswith(".gz"):
                tgt_files.append(Path(os.path.join(root, file)))

    comparable_files = [(src_file, target_file)
                        for src_file in src_files
                        for target_file in tgt_files
                        if src_file.name == target_file.name]

    for src_file, target_file in comparable_files:
        source = json.loads(unzip(src_file))
        target = json.loads(unzip(target_file))

        changes = compare_content(source['value'], target['value'])

        with open(backup_path + src_file.name[:-2] + 'json', 'w') as file:
            json.dump(changes, file, indent=4)


def compare_content(source: list, target: list) -> dict:

    source_items_map = {source_item['id']: source.index(source_item) for source_item in source}
    target_items_map = {target_item['id']: target.index(target_item) for target_item in target}

    changes_dict = {
        'Deleted': [],
        'Added': [],
        'ChangedAttribute': [],
    }

    source_items_set = set(source_items_map.keys())
    target_items_set = set(target_items_map.keys())

    for item in source_items_set & target_items_set:
        pair = source[source_items_map[item]], target[target_items_map[item]]
        changed_attribute = find_changed_attributes(*pair)
        if len(changed_attribute) > 0:
            changes_dict['ChangedAttribute'] += changed_attribute

    for item in source_items_set - target_items_set:
        added = {
            'id': item,
            'userType': source[source_items_map[item]]['userType'],
        }
        changes_dict['Added'].append(added)

    for item in target_items_set - source_items_set:
        deleted = {
            'id': item,
            'userType': target[target_items_map[item]]['userType'],
        }
        changes_dict['Deleted'].append(deleted)

    return changes_dict


def find_changed_attributes(source_item: dict, target_item: dict) -> list:
    changed_attribute = []
    for key in source_item:
        if source_item[key] != target_item[key]:
            change = {
                'id': source_item['id'],
                'attribute': key,
                'oldValue': target_item[key],
                'newValue': source_item[key],
            }
            changed_attribute.append(change)
    return changed_attribute


def unzip(path: Path) -> bytes:
    with open(path, 'rb') as file:
        data = file.read()
        return gzip.decompress(data)
