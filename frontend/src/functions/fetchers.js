const getAllData = async (url) => {
    let result = await fetch(url)
      let data = await result.json()
      return await data
}

export {
    getAllData
}