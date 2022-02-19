from flight import flightObject
import json
import glob
import os


def load_list_of_json(folder_name):
    list_of_flight_obj = []
    flight_files = list(glob.glob(f"{folder_name}/" + "*"))

    for flight_file in flight_files:
        flight_obj = load_file_to_obj(flight_file)
        list_of_flight_obj.append(flight_obj)
    return list_of_flight_obj


def load_file_to_obj(file_name):
    """
    :param file_name: get a file
    :return: an object
    """
    with open(f'{file_name}', 'rb') as file_obj:
        data = json.load(file_obj)

    flight_object = flightObject(flight_company=data['flight_company'],
                                 flight=data['flight'],
                                 landing_from=data['landing_from'],
                                 terminal=data['terminal'],
                                 scheduled_time=data['scheduled_time'],
                                 updated_time=data['updated_time'],
                                 status=data['status'])

    return flight_object


def data_list_to_dict(data_list):
    """
    :param data_list: get list of objects
    :return: a dict from objects
    """
    data_dict = {}

    for obj in data_list:
        key = (obj.flight_company + obj.flight + obj.terminal + obj.scheduled_time.replace('/', '').replace(':',
                                                                                                            '')).replace(
            " ", "")

        data_dict[key] = {'flight': obj.flight, 'flight_company': obj.flight_company, 'landing_from': obj.landing_from,
                          'terminal': obj.terminal, 'scheduled_time': obj.scheduled_time,
                          'updated_time': obj.updated_time, 'status': obj.status}

    return data_dict


# def load_files_from_folder(folder_name):
#     object_list = []
#     flight_files = list(glob.glob(f"{folder_name}/" + "*"))
#     file_names = ['https://' + os.path.basename(x).replace('.json', '').replace('_', '/') for x in articles_files]
#     for flight_file in flight_files:
#         object = load_file_to_obj(flight_file)
#         object_list.append(object)
#     return object_list

def save_file(obj, folder_name):
    """
    :param obj: object
    :param folder_name: folder to save file at
    save file at folder
    """
    key = (obj.flight_company + obj.flight + obj.terminal + obj.scheduled_time.replace('/', '').replace(':',
                                                                                                        '')).replace(
        " ", "")

    data_dict = {'flight': obj.flight, 'flight_company': obj.flight_company, 'landing_from': obj.landing_from,
                 'terminal': obj.terminal, 'scheduled_time': obj.scheduled_time,
                 'updated_time': obj.updated_time, 'status': obj.status}

    with open(f'{folder_name}/{key}.json', 'w') as file_obj:
        json.dump(data_dict, file_obj)


def save_list_of_obj(obj_list, folder_name):
    for obj in obj_list:
        save_file(obj, folder_name)
