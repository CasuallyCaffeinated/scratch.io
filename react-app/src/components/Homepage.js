import React from "react"
import GameJamBox from "./gamejams/GameJamBox";
import GameBox from "./games/GameBox"



import {
    Flex,
    Box,
    Heading
} from "@chakra-ui/react"


export default function Homepage() {
        var path = process.env.PUBLIC_URL;
        var image = "logo_W.png";
        var image2 = "logo_H.png";
        var image3 = "logo_I.png";
        var image4 = "logo_S.png";
        var image5 = "logo_K.png";
    return (
        <Flex h="100vh" w="100vw" direction="column">
        <Box
        className="hp-main-img"
        >
             <img src={path + image}/>
             <img src={path + image2}/>
             <img src={path + image3}/>
             <img src={path + image4}/>
             <img src={path + image5}/>
        </Box>
        <Box>
            <Heading>
            <h1>
                Genre
            </h1>
            </Heading>
            <GameJamBox />
        </Box>
        <Box>
        <Heading>
            <h1>
                Genre
            </h1>
            </Heading>
            <GameBox />
        </Box>

        </Flex>
    )
}
