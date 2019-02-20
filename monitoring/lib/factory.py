from monitoring.code.rest import monitor_rest
from monitoring.code.redis_server import check_redis_connection


SERVICES_LIST = {
    'rest': monitor_rest,
    'redis': check_redis_connection
}


def get_factory_method(service_type):
    if not service_type:
        raise Exception("Please provide a valid service type. Implemented Services - %s",
                        SERVICES_LIST)

    if service_type.lower() not in SERVICES_LIST:
        raise Exception("The service type %s has not been implemented.." % service_type)

    return SERVICES_LIST[service_type]
