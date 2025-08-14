export const loginReducer = (state, action) => {
  switch(action.type) {
    case 'EMAIL':
      return { ...state, email: action.payload };
    case 'PASSWORD':
      return { ...state, password: action.payload };
    case 'SetUser':
      return {...state, user: action.payload.user, token: action.payload.token , isAuth: true}
    case 'Rest':
      return {email: '', password: '', user: null , token: null,isAuth:false}
    default:
      return state;
  }
};