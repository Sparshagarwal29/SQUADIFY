import '../../../App.css'
import { Link, useNavigate } from 'react-router-dom'
import { useLogin } from '../../context/login-context';

const Login = () => {
    const navigate = useNavigate();
    const {loginDispatch} = useLogin();

    const onEmailChange = (e) =>{
        loginDispatch({
            type: 'Email',
            payload: {
                value: e.target.value
            }
        })
    }
    const onPasswordChange = (e) =>{
        loginDispatch({
            type: 'Password',
            payload: {
                value: e.target.value
            }
        })
    }
    
    const handleFormSubmit = (e) => {
        e.preventDefault();
        navigate('/DashBoard');
    }
    return (
        <form onSubmit={handleFormSubmit}>
            <nav className="login-nav">
                <span>Find Team</span>
                <span>Login</span>
            </nav>
            <div className="login-middle">
                <h1>Login</h1>
                <input onChange={onEmailChange} type="email" name="Email" required placeholder="Email"/>
                <input  onChange = {onPasswordChange} type="password" name="Password" required placeholder="Password"/>
                <button type="submit" className="login-btn">Login</button>
                <div className="signup-section">
                    <span className="signup-text">Don't have an account?</span>
                    <span className="signup-link">
                        <button type="button" className="signup-btn">Sign up</button>
                    </span>
                </div>
            </div>
        </form>
    )
}

export default Login