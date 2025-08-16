import { useState } from "react"
import './Team.css'



const HandleHTML = ({type,field,member,index, handleMemberChange}) =>{  
    return(
        <div className= {`${field}-Team-section`}>
            <label htmlFor={`${field}-${index}`}>
                {field.charAt(0).toUpperCase() + field.slice(1)}::
            </label>
            <input 
                type={type}
                id= {`${field}-${index}`}
                value={member[field]}
                onChange={(e) => handleMemberChange(index , field ,e.target.value)} 
                placeholder={`Enter you Team Member's ${field}`}
                className="Team-Info"
            />
        </div>
    )
}

const CreateTeam = () =>{
    const[teamMembers, setTeamMembers] = useState([
        {name: '' , role: '',email: '' , contact: '', techstack: '', hobbies:'' },
        {name: '' , role:'',email: '' , contact: '', techstack: '', hobbies:'' }
    ]);
    const[teamsize, setteamSize] = useState(2);
    const handleTeamSize =(e) =>{
        const size = parseInt(e.target.value,10);
        setteamSize(size)
        const newMembers = Array.from({ length: size }, () => ({ 
            name: '', 
            role: '', 
            email: '',
            contact: '', 
            techstack: '', 
            hobbies:''
        }));
        setTeamMembers(newMembers);
    }
    const handleMemberChange = (index,field,value) =>{
        const updateteammember = [...teamMembers]
        updateteammember[index] = {
            ...updateteammember[index],
            [field]: value
        };
        setTeamMembers(updateteammember);
    };
    const validateForm = () =>{
        console.log("done");
    }
    return(
        <>
            <form onSubmit={validateForm} >
                <div className="Team-Name">
                    <h1 className="Team-member-h1">Create Your Team</h1>
                    <input 
                        type="text"
                        required
                        placeholder="Enter your team name"
                        className="Team-Name-input"
                    />
                </div>
                <div>
                    <label className="Team-size" >
                        Team Size:
                    </label>
                    <select 
                        name="Team-member"  
                        value={teamsize}
                        onChange={handleTeamSize}
                        className="Team-member-select"
                    >
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                </div>
                <div className="Team-member-About">
                    <h3 className="Team-member-h3"> Team Member Information</h3>
                    {teamMembers.map((member,index)=>(   
                        <div key={index}>
                            <h4 className="Team-member-h4" >Members: {index+1}</h4>
                            <div className="team-section">
                                <HandleHTML
                                    type = "text"
                                    field = "name"
                                    member = {member}
                                    index = {index}
                                    handleMemberChange={handleMemberChange}
                                />
                                <HandleHTML
                                    type = "text"
                                    field = "role"
                                    member = {member}
                                    index = {index}
                                    handleMemberChange={handleMemberChange}
                                />
                                <HandleHTML
                                    type = "email"
                                    field = "email"
                                    member = {member}
                                    index = {index}
                                    handleMemberChange={handleMemberChange}
                                />
                                <HandleHTML
                                    type = "tel"
                                    field = "contact"
                                    member = {member}
                                    index = {index}
                                    handleMemberChange={handleMemberChange}
                                />
                                <HandleHTML
                                    type = "text"
                                    field = "techstack"
                                    member = {member}
                                    index = {index}
                                    handleMemberChange={handleMemberChange}
                                />
                                <HandleHTML
                                    type = "text"
                                    field = "hobbies"
                                    member = {member}
                                    index = {index}
                                    handleMemberChange={handleMemberChange}
                                />
                            </div>
                        </div>
                    ))}
                </div>
                <div className="submit">
                    <button className="submit-btn">
                        Submit form
                    </button>
                </div>
            </form>
        </>
    )

}
export default CreateTeam