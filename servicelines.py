import random

import config

layout = config.LAYOUT
discipline = config.DISCIPLINE

def get_service_line_shelf(service_line):
    if layout == 'Current Layout':
        match service_line:
            case 'HF':
                return random.choice([42, 43, 44, 45, 46, 47, 48])
            case 'Anesthesiology':
                return random.choice([3, 4])
            case 'Cardio' | 'Cardiovascular':
                return random.choice([19, 14, 20])
            case 'Colorectal':
                return random.choice([1, 2])
            case 'Electrophysiology':
                return random.choice([0, 9])
            case 'Gastroenterology':
                return random.choice([3, 4])
            case 'General Surgery':
                return random.choice([30, 31, 32])
            case 'Gynecology':
                return random.choice([27, 28, 29])
            case 'Neuro' | 'Neurosurgery':
                return random.choice([38, 37, 36])
            case'Obstetrics':
                return random.choice([3, 4])
            case 'Oncology':
                return random.choice([6, 12])
            case 'Ophthalmology':
                return 5
            case 'Oral Surgery':
                return random.choice([8, 7])
            case 'Ortho' | 'Orthopedic Surgery':
                return random.choice([23, 22, 21])
            case 'Otolaryngology':
                return random.choice([41, 40, 39])
            case 'Plastic Surgery':
                return random.choice([10, 11])
            case 'Podiatry':
                return random.choice([16, 17, 18])
            case 'Pulmonology':
                return 13
            case 'Thoracic Surgery':
                return 5
            case 'Urology':
                return random.choice([24, 25, 26])
            case 'Vasc' | 'Vascular Surgery':
                return random.choice([33, 34, 35])
            case _:
                print(f'Service line \'{service_line}\' not defined')
    if layout == 'Patterson Pope':
        match service_line:
            case 'HF':
              return random.randint(61, 116)  
            case'Anesthesiology':
                return random.choice([8, 10])
            case 'Cardio' | 'Cardiovascular':
                return random.choice([32, 30, 28, 26])
            case 'Colorectal':
                return random.choice([14, 12])
            case 'Electrophysiology':
                return random.choice([15, 13])
            case 'Gastroenterology':
                return random.choice([4, 5])
            case 'General Surgery':
                return random.choice([49, 47, 45, 43])
            case 'Gynecology':
                return random.choice([34, 35, 53, 51])
            case 'Neuro' | 'Neurosurgery':
                return random.choice([54, 52, 55, 56])
            case 'Obstetrics':
                return 8
            case 'Oncology':
                return random.choice([16, 18, 20])
            case 'Ophthalmology':
                return random.choice([4, 10])
            case 'Oral Surgery':
                return random.choice([11, 9])
            case 'Ortho' | 'Orthopedic Surgery':
                return random.choice([33, 36, 39, 42])
            case 'Otolaryngology':
                return random.choice([57, 58, 59, 60])
            case 'Plastic Surgery':
                return random.choice([22, 23, 21])
            case 'Podiatry':
                return random.choice([17, 19])
            case 'Pulmonology':
                return random.choice([1, 2])
            case 'Thoracic Surgery':
                return random.choice([29, 27, 25])
            case 'Urology':
                return random.choice([37, 38, 40, 41])
            case 'Vasc' | 'Vascular Surgery':
                return random.choice([50, 48, 46, 44])
            case _:
                print(f'Service line \'{service_line}\' not defined')
    else:
        print(f'Service lines not defined for layout \'{layout}\'')