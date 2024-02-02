import Hero from "../components/Hero/Hero"
import ChooseUs from "../components/ChooseUs"
import Trainers from "../components/Trainers"
import Testimonials from "../components/Testimonials"
import Gallery from "../components/Gallery"


function Home(){
    return(
        <>
            <Hero/>
            <ChooseUs/>
            <Trainers/>
            <Testimonials/>
            <Gallery/>
        </>
    )
}

export default Home