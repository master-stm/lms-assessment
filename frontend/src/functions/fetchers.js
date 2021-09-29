const getAllData = async (url) => {
    let result = await fetch(url)
      let data = await result.json()
      return await data
}

const addBook = async (url, dataObject) => {

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

export {
    getAllData,
    addBook
}