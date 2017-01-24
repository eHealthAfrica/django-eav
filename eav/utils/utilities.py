from django.conf import settings


class Utils(object):
    ENTITY_ID_TYPES = {
        'uuid': 'entity_uuid',
        'int': 'entity_id'
    }

    def get_eav_entity_id_type(self):
        key = 'int'
        if hasattr(settings, 'EAV_ENTITY_ID_TYPE'):
            key = settings.EAV_ENTITY_ID_TYPE
        return self.ENTITY_ID_TYPES.get(key, 'int')
