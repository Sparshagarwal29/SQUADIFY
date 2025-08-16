import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './components/pages/Home/home.jsx'
import Login from './components/pages/Login/Login.jsx'
import Dashboard from './components/pages/Dashboard/dashboard.jsx'
import { Signup } from './components/pages/sign_up/index.jsx'
import CreateTeam from './components/pages/Team/CreateTeam.jsx'
function App() {

  return (
    <>
        <div className='App'>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Login" element={<Login />} />
            <Route path='/DashBoard' element ={<Dashboard/>} />
            <Route path='/SignUP' element ={<Signup/>} />
            <Route path='/createTeam' element ={<CreateTeam/>} />
          </Routes>
        </div>
    </>
  )
}

export default App
