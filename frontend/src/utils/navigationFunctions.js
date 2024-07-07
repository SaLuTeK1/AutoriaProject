import {SetURLSearchParams} from "react-router-dom";


export const prev = (setQuery) =>{
    setQuery(prev=>{
        prev.set('page',`${+prev.get('page')-1}`)
        return prev
    })
}
export const next = (setQuery) =>{
    setQuery(prev=>{
        prev.set('page',`${+prev.get('page')+1}`)
        return prev
    })
}