import xmlrpc.client
url = 'http://localhost:8070'
db = 'odoo14'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password,
    'simplify_licences.simplify_licences', 'check_access_rights',
    ['read'], {'raise_exception': False})
keys = models.execute_kw(db, uid, password,
    'simplify_licences.simplify_licences', 'search',
    [[['active', '=', True]]])

print(keys)

record = models.execute_kw(db, uid, password,
    'simplify_licences.simplify_licences', 'read', [keys]) # GET ALL FIELDS FROM KEYS=IDS


records_fields_only = models.execute_kw(db, uid, password,
    'simplify_licences.simplify_licences', 'read',
    [keys], {'fields': ['name', 'value', 'partner_id', 'date_start', 'date_end', 'active']}) # GET ONLY SPECIFIC FIELDS
print(records_fields_only)

new_id = models.execute_kw(db, uid, password, 'simplify_licences.simplify_licences', 'create', [{
    'name': "New machine1", "value" : 'LICENCE#3', 'date_start' : '2021-09-23', 'date_end': '2021-11-11'
}]) # CREATE A RECORD IF NOT EXISTS

print(new_id)