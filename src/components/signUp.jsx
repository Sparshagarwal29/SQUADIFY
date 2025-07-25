import '../App.css'

const  SignUp =() => {
    return(
        <>
            <nav className="signup-nav">
                <span>Find Team</span>
                <span>Sign Up</span>
            </nav>
            <div className="signup-middle">
                <h1>sign up</h1>
                <input type="text" name="" id="" placeholder="Name"/>
                <input type="email" name="" id="" placeholder="Email"/>
                <input type="password" name="" id="" placeholder="Password"/>
                <input type="password" name="" id="" placeholder="Confirm Password"/>
                <button className="signup-btn">Sign Up</button>
                <div className="login-section">
                    <span className="login-text">Already have an account?</span>
                    <span className="login-link">
                        <button className="login-btn">Login</button>
                    </span>
                </div>

            </div>
        </>
    )
}

export default SignUp