import '../../../App.css'
import { Link, useNavigate } from 'react-router-dom'
import { useLogin } from '../../context/login-context';
import api from '../../request/request';
import { useState } from 'react';
const Login = () => {
    const navigate = useNavigate();
    const {email,password,loginDispatch} = useLogin();
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const onEmailChange = (e) =>{
        loginDispatch({
            type: 'EMAIL',
            payload: {
                value: e.target.value,
            }
        });
        setError('');
    };
    const onPasswordChange = (e) =>{
        loginDispatch({
            type: 'PASSWORD',
            payload: {
                value: e.target.value
            }
        });
        setError('');
    };
    const validateForm = () =>{
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        console.log('Validating email:', email);
        if (!emailRegex.test(email)) {
            setError('Please enter a valid email address');
            return false;
        }
        if (password.length < 8) {
            setError('Password must be at least 8 characters long');
            return false;
        }
        return true;
      };
    const handleFormSubmit = async(e) => {
        e.preventDefault();
        setError('')
        // if(!validateForm()) return
        setIsLoading(true);
        try{
            const response = await api.post('/login',{username:email,password})
            const{access_token} = response.data
            localStorage.setItem('token',access_token);
            loginDispatch({
                type: "SetUser",
                payload: {user:{email},token: access_token}
            });
            navigate('/DashBoard');
        } catch(error){
            if (error.response?.status === 401) {
                setError('Invalid email or password');
            } else {
                setError('An error occurred. Please try again.');
            }
        } finally {
            setIsLoading(false);
        }
    }
    return (
        <form onSubmit={handleFormSubmit}>
            <nav className="login-nav">
                <span>Find Team</span>
                <span>Login</span>
            </nav>
            <div className="login-middle">
                <h1>Login</h1>
                {error && <div className="error-message" style={{ color: 'red', marginBottom: '10px' }}>{error}</div>}
                <input onChange={onEmailChange} type="email" 
                    // value={email} 
                    name="Email" required placeholder="Email" aria-label="Email address"/>
                <input  onChange = {onPasswordChange} type="password" 
                    // value={password}    
                    name="Password" required placeholder="Password"/>
                <button type="submit" className="login-btn" disabled={isLoading}>{isLoading ? 'Logging in...' : 'Login'}</button>
                <div className="signup-section">
                    <span className="signup-text">Don't have an account?</span>
                    <span className="signup-link">
                        <Link to="/SignUP">
                            <button type="button" className="signup-btn">Sign up</button>
                        </Link>
                    </span>
                </div>
            </div>
        </form>
    )
}

export default Login