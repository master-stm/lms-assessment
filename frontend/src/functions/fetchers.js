const getAllData = async (url) => {
    let result = await fetch(url)
    let data = await result.json()
    return await data
}

const getData = async (url) => {
    
    let res = await fetch(url)
    let data = await res.json()  
    return await data;
        
}

const addData = async (url, dataObject) => {

    try {
        await fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(dataObject)
    })
    } catch (error) {
        console.error(error)
    }
    
}

const editData = async (url, dataObject) => {

    try {
        fetch(url, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(dataObject),
          })
    } catch (error) {
        console.error(error)
    }

}

export {
    getAllData,
    getData,
    addData,
    editData
}