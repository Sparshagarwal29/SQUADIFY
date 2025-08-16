import { Search } from 'lucide-react'
import { Link } from 'react-router-dom'

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
                <div>
                    <Link to="/CreateTeam">
                        <button type="button">
                                createTeam
                        </button>
                    </Link>
                </div>
            </div>
        
        </>
    )

}
export default Dashboard