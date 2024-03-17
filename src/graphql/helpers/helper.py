from sqlalchemy.inspection import inspect

def getOnlySelectedFields(dbBaseclassName, info):
    dbRelationFields = inspect(dbBaseclassName).relationships.keys()
    selectedFields = [field.name for field in info.selected_fields[0].selections if field.name not in dbRelationFields]
    return selectedFields
    
def getValidData(modelDataObject, modelClass):
    dataDict = {}
    for column in modelClass.__table__.columns:
        try:
            dataDict[column.name] = getattr(modelDataObject,column.name)
        except:
            pass
    return dataDict