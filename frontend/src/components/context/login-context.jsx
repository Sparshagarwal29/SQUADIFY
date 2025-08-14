import {createContext, useContext , useReducer } from "react";
import { loginReducer } from "../../Reducers/loginReducer";

const loginContext = createContext();
const LoginProvider = ({children}) =>{
    const initialState ={
        email: '',
        password: '',
        user: null,
        token: null,
        isAuth:false
    }
    const [{email,password,user,token,isAuth},loginDispatch] = useReducer(loginReducer,initialState)
    return(
        <loginContext.Provider value={{email,password,user,token,isAuth,loginDispatch}} >
            {children}
        </loginContext.Provider>
    )
}
const useLogin = () =>useContext(loginContext)


export {LoginProvider,useLogin}
