import { useState } from "react";
import toast from "react-hot-toast";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import Button from '@mui/material/Button';

export default function MultipleChoice({ multiQuestion }) {
    
    const [studentAnswer, setStudentAnswer] = useState("");
    const choiceChange = (e) => {
        setStudentAnswer(e.target.value);
    }
    
    if (!multiQuestion) {
        return null;
    }

    let answers = multiQuestion.options.slice();
    
    const clickAnswer = () => {
        if (studentAnswer === multiQuestion.answer)  {
            toast.success("You win!!");
        } else {
            toast.error("Incorrect, try again!");
        }
    }

    return (
        <FormControl>
            <FormLabel id="multi-choice-radio-group">
                {multiQuestion.question}
            </FormLabel>
            <RadioGroup
                aria-labelledby="multi-choice-radio-group"
                name="multi-choice-question"
                onChange={choiceChange}
            >
                <FormControlLabel
                    value={answers[0]}
                    control={<Radio />}
                    label={answers[0]}
                />
                <FormControlLabel
                   value={answers[1]}
                   control={<Radio />}
                   label={answers[1]}
                />
                <FormControlLabel
                    value={answers[2]}
                    control={<Radio />}
                    label={answers[2]}
                />
                <FormControlLabel
                    value={answers[3]}
                    control={<Radio />}
                    label={answers[3]}
                />
            </RadioGroup>
            <Button onClick={clickAnswer} variant="contained">Submit</Button>
        </FormControl>
    );
}

