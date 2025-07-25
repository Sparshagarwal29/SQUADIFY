import TopHead from './nav.jsx'
import { Link } from 'react-router-dom' 
import '../App.css'
function Home() {


  return (
    <>
      <div>
        <div className="header">
        <label>
            <span> <button> profile </button></span>  <span><button>sign up</button></span>   <span><button>search</button></span>
        </label>
        </div>
        <div className='middleSection'>
          <h1> Find your hackathon team here </h1>
          <Link to="/SignUp">
            <button className='start_btn'>GETTING STARTED</button>
          </Link>
        </div>

      </div>
    </>
  )
}

export default Home