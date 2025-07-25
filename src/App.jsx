import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './components/home.jsx'
import SignUp from './components/signUp.jsx'
function App() {

  return (
    <>
        <div className='App'>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/SignUp" element={<SignUp />} />
          </Routes>
        </div>
    </>
  )
}

export default App
