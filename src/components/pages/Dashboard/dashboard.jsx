import { Search } from 'lucide-react'

const Dashboard =() =>{
    return (
        <>
            <nav className="Dashboard">
                <button className='DASH-home'>Home</button>
                <label className='team-home'>find team <Search size={10}/> </label>
            </nav>
            <div className="middle_Dash">
                <h1>Dashboard</h1>
                <div className="cart">
                   <p>Here would be your profile</p>
                </div>
                <div className="profile">
                    <h2>Team</h2>
                    <p>Here is your team </p>
                </div>
            </div>
        
        </>
    )

}
export default Dashboard