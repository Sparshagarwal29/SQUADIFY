import '../../../App.css'
export const Signup =() =>{
    return (
        <>
            <form>
            <nav className="SignUp-nav">
                <span>Find Team</span>
                <span>Login</span>
            </nav>
            <div className="SignUp-middle">
                <h1>Login</h1>
                <input  type="name" name="Email" required placeholder="Name"/>
                <input  type="email" name="Email" required placeholder="Email"/>
                <input  type="number" name="Email" required placeholder="Number"/>
                <input   type="password" name="Password" required placeholder="Password"/>
                <button  type="submit" className="Signup-Page-btn">SignUP</button>
            </div>
        </form>
        </>
    
    )
}