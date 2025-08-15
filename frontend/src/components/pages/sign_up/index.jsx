import { useState } from 'react';
import '../../../App.css'
import api from '../../request/request';
import {useNavigate} from 'react-router-dom';
export const Signup =() =>{
    const navigate = useNavigate();
    const[name,setName] = useState('')
    const[email,setEmail] = useState('')
    const[password,setPassword] = useState('')
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState('');

    const validateform = () =>{
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(!emailRegex.test(email)){
           setError("Please enter a valid email address");
            return false;
        }
        if(password.length < 8){
            setError("Password must be at least 8 characters long");
            return false;
        }
        if(name.length < 2){
            setError("Name must be at least 2 characters long");
            return false;
        }
        return true;
    }
    const handleFormsubmit = async(e) =>{
        e.preventDefault();
        setError('');
        if(!validateform()) return
        setIsLoading(true);

        try {
            const response = await api.post('/User',{
                username: name,
                email: email ,
                password: password
            })
            console.log("User created successfully", response.data);   
            navigate('/login');

        } catch (error) {
            if (error.response?.status === 409) { 
                setError("This email is already registered.");
            } else if (error.response?.status === 422) { 
                setError("Invalid data. Please check your inputs.");
            } else {
                setError(error.response?.data?.detail || "An unexpected error occurred. Please try again.");
            }
        } finally{
            setIsLoading(false);
        }
    }
    return (
        <>
            <form onSubmit={handleFormsubmit}>
            <nav className="SignUp-nav">
                <span>Find Team</span>
                <span>Login</span>
            </nav>
            <div className="SignUp-middle">
                <h1>Login</h1>
                <input  
                    type="text"
                    name="Name" 
                    required 
                    placeholder="Name"
                    value={name}
                    onChange={(e) =>setName(e.target.value)}
                />
                <input  
                    type="email" 
                    name="Email" 
                    required 
                    value={email}
                    placeholder="Email"
                    onChange={(e) =>setEmail(e.target.value)}
                />
                <input  
                    type="password" 
                    name="Password" 
                    required 
                    value={password}
                    placeholder="Password"
                    onChange={(e) =>setPassword(e.target.value)}
                />
                <button type="submit" className="Signup-Page-btn" disabled={isLoading}>
                    {isLoading ? 'Creating Account...' : 'Sign Up'}
                </button>
            </div>
        </form>
        </>
    
    )
}