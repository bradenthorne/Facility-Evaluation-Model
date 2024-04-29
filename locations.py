import random

import pandas as pd

import config
from servicelines import get_service_line_shelf

layout = config.LAYOUT
discipline = config.DISCIPLINE

def define_supply_locations(item_list, service_line_dict):
    if layout == 'Current Layout':
        match discipline:
            case 'Current':
                current_location_df = pd.read_excel('Current Supply Locations.xlsx', sheet_name='Supply Locations with Fill')
                return {row['Item Number']: row['Location'] for _, row in current_location_df.iterrows()}
            case 'Random':
                return {item_number: random.randint(0, 48) for item_number in item_list}
            case 'Frequency':
                frequency_locations = pd.read_excel(f'{layout} High Frequency Locations.xlsx')
                return {row['Item']: row['Shelf'] for _, row in frequency_locations.iterrows()}
            case 'Service Lines':
                return {item_number: get_service_line_shelf(service_line) for item_number, service_line in service_line_dict.items()}
            case _:
                print(f'Discipline \'{discipline}\' not found for layout \'{discipline}\'')
    if layout == 'Patterson Pope':
        match discipline:
            case 'Random':
                return {item_number: random.randint(0, 116) for item_number in item_list}
            case 'Frequency':
                frequency_locations = pd.read_excel(f'{layout} High Frequency Locations.xlsx')
                return {row['Item']: row['Shelf'] for _, row in frequency_locations.iterrows()}
            case 'Service Lines':
                return {item_number: get_service_line_shelf(service_line) for item_number, service_line in service_line_dict.items()}
            case _:
                print(f'Discipline \'{layout}\' not found for layout \'{layout}\'')

def apply_supply_locations(pick_list_df, location_dict):
    return pick_list_df.applymap(lambda x: location_dict[x] if x in location_dict.keys() else 1000).values.tolist()
