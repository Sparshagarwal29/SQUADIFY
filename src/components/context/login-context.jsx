import {createContext, useContext , useReducer } from "react";
import { loginReducer } from "../../Reducers/loginReducer";

const loginContext = createContext();
const LoginProvider = ({children}) =>{
    const initialState ={
        email: '',
        password: ''
    }
    const [{email,password},loginDispatch] = useReducer(loginReducer,initialState)
    return(
        <loginContext.Provider value={{email,password,loginDispatch}} >
            {children}
        </loginContext.Provider>
    )
}
const useLogin = () =>useContext(loginContext)


export {LoginProvider,useLogin}
