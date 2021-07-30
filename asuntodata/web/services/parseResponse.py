import functools
import itertools


def parseResponse(data):

    if (data == None):
        return None
    dimension = None
    values = None

    try:
        dimension = data['dataset']['dimension']
        values = data['dataset']['value']
    except:
        return None

    # zipsObj = dimension.Postinumero.category.index
    ids = dimension['id']

    sizeArray = dimension['size']

    def multiply(a, b):
        return a*b
    itemCombs = functools.reduce(multiply, sizeArray)

    count = 0
    i = 0

    def createObject(obj, type, structure, objectsList, pos, values, count):
        objElement = {}

        while (pos < len(structure)):

            labels = objectsList[structure[pos]]['category']['label']
            labelIndeces = objectsList[structure[pos]]['category']['index']

            labelsArr = []
            for i, index in enumerate(labelIndeces):
                labelsArr.append([i, labels[list(labels)[i]]])

            def sortLabelsByIndex(e):
                return e[0]

            labelsArr.sort(key=sortLabelsByIndex)

            for item in labelsArr:
                objElement[item[1]] = ""

            if (len(obj) == 0):
                obj = objElement
            else:
                for k, v in obj.items():
                    obj[k] = objElement

            pos = pos + 1

            if pos == len(structure):
                # print("FINAL-test")
                # print(pos)
                for objItem in objElement:
                    # print(count)
                    count = count + 1

            return createObject(
                objElement,
                type,
                structure,
                objectsList,
                pos,
                values,
                count
            )

    dataObject = {'data': ''}
    createObject(dataObject, "item", ids, dimension, 0, values, 0)

    dataObject = dataObject['data']

    def createTotalObject(obj, structure):
        objKeys = list(structure.keys())
        # print(structure)
        # print("test")

        for key in objKeys:
            if len(objKeys) == 0:
                # print("TEST-OLI-0")
                obj[key] = []
                obj[str(key+'_count')] = []
                obj[str(key+'__zip')] = []

            else:
                 print("TEST-OLI-YLI-0")

    """
    const createTotalObject = (obj, structure) = > {
        objKeys = Object.keys(structure)

        for (const key in objKeys) {
            if (Object.keys(structure[objKeys[key]]).length === 0) {
                Object.defineProperty(obj, objKeys[key], {
                    value: [],
                    writable: true,
                    enumerable: true,
                })
                Object.defineProperty(obj, objKeys[key] + "_count", {
                    value: [],
                    writable: true,
                    enumerable: true,
                })
                Object.defineProperty(obj, objKeys[key] + "_zip", {
                    value: [],
                    writable: true,
                    enumerable: true,
                })
            } else {
                Object.defineProperty(obj, objKeys[key], {
                    value: {},
                    writable: true,
                    enumerable: true,
                })
            }

            createTotalObject(obj[objKeys[key]], structure[objKeys[key]])
        }
    } """

    totalObject = {'data': {}}

    if list(dataObject.keys())[0]:
        createTotalObject(totalObject['data'],
                          dataObject[list(dataObject.keys())[0]])

    """ if ( dataObject[Object.keys(dataObject)[0]] ) {
        createTotalObject(totalObject.data,
                          dataObject[Object.keys(dataObject)[0]])
    } """

     #print("MY_TESTxx")
    # print(totalObject)
    return dataObject
    '''
    resArr = []

    const loopValues = (
        obj,
        totalObject,
        resObject,
        values,
        sizeArray,
        round,
        objectRound,
        testArr
    ) = > {
        sizes = [...sizeArray]
        objectRound = objectRound + 1
        sizes.shift()

        itemCombs = sizes.reduce(function(a, b) {
            return a * b
        }, 1)

        objKeys = Object.keys(obj)

        loopCount = 0
        newRound = 0
        for (const key in objKeys) {
            Object.defineProperty(resObject, objKeys[key], {
                value: {},
                writable: true,
                enumerable: true,
            })
            newRound = round + loopCount * itemCombs

            // When value is empty string we are are the end of the object tree. -> save value to the variable
            if (obj[objKeys[key]] == = "") {
                treeCount = 0

                for (const item in obj) {
                    testArr.push(values[newRound + treeCount])
                    try {
                        if (true) {
                            if (values[newRound + treeCount] == = None) {
                                Object.defineProperty(resObject, item, {
                                    value: "None",
                                    writable: true,
                                    enumerable: true,
                                })
                            } else {
                                Object.defineProperty(resObject, item, {
                                    value: values[newRound + treeCount],
                                    writable: true,
                                    enumerable: true,
                                })

                                totalObject[item].push(
                                    values[newRound + treeCount])
                                if (item === "Neliöhinta (EUR/m2)") {
                                    totalObject[item + "_count"].push(
                                        values[newRound + treeCount + 1]
                                    )
                                }
                            }
                        }
                    } catch(error) {}

                    treeCount = treeCount + 1
                }
                break
            }

            totalObjectToSend

            if (objectRound == = 1) {
                totalObjectToSend = totalObject.data
            } else if (objectRound > 1) {
                totalObjectToSend = totalObject[objKeys[key]]
            }

            loopValues(
                obj[objKeys[key]],
                totalObjectToSend,
                resObject[objKeys[key]],
                values,
                sizes,
                newRound,
                objectRound,
                testArr
            )
            loopCount++
        }
        // return resObject
    }

    testArr = []
    sizeArrayCombs = [...sizeArray]

    newObject = {data: {}}

    resArr = loopValues(
        dataObject,
        totalObject,
        newObject.data,
        values,
        sizeArrayCombs,
        0,
        0,
        testArr
    )

    newObject.data["total"] = totalObject

    //calculate averages for regions

    newObject.data.total = newObject.data.total.data

    keysLayer1 = [] // Object.keys(newObject.data.total)

    Object.getOwnPropertyNames(newObject.data.total).forEach((key)= > {
        keysLayer1.push(key)
    })
    for (const layer1 in keysLayer1) {
        keysLayer2 = [
        ] // Object.keys(newObject.data.total[keysLayer1[layer1]])
        Object.getOwnPropertyNames(
            newObject.data.total[keysLayer1[layer1]]
        ).forEach((key)=> {
            keysLayer2.push(key)
        })

        for (const layer2 in keysLayer2) {
            keysLayer3 = [
            ] // Object.keys(newObject.data.total[keysLayer1[layer1]])
            Object.getOwnPropertyNames(
                newObject.data.total[keysLayer1[layer1]][keysLayer2[layer2]]
            ).forEach((key)= > {
                keysLayer3.push(key)
            })

            for (const layer3 in keysLayer3) {
                countArray =
                newObject.data.total[keysLayer1[layer1]][keysLayer2[layer2]][
                    keysLayer3[layer3]
                ]["Neliöhinta (EUR/m2)_count"]
                countSum = countArray.reduce(function(a, b) {
                    return a + b
                }, 0)

                priceArray =
                newObject.data.total[keysLayer1[layer1]][keysLayer2[layer2]][
                    keysLayer3[layer3]
                ]["Neliöhinta (EUR/m2)"]
                avgPrice = 0
                for (const item in priceArray) {
                    avgPrice =
                    avgPrice + (priceArray[item] * countArray[item]) / countSum
                }

                newObject.data.total[keysLayer1[layer1]][keysLayer2[layer2]][
                    keysLayer3[layer3]
                ]["avg_Neliöhinta (EUR/m2)"] = avgPrice

                countTotalArray =
                newObject.data.total[keysLayer1[layer1]][keysLayer2[layer2]][
                    keysLayer3[layer3]
                ]["Kauppojen lukumäärä"]
                countTotalSum = countTotalArray.reduce(function(a, b) {
                    return a + b
                }, 0)

                newObject.data.total[keysLayer1[layer1]][keysLayer2[layer2]][
                    keysLayer3[layer3]
                ]["total_Kauppojen lukumäärä"] = countTotalSum
            }
        }
    }
    return newObject
    '''

    return data
