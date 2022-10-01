import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";

export default function MultipleChoice({ multiQuestion }) {
    if (!multiQuestion) {
        return null;
    }

    let answers = multiQuestion.options;
    // console.log(multiQuestion);

    return (
        <FormControl>
            <FormLabel id="multi-choice-radio-group">
                {multiQuestion.question}
            </FormLabel>
            <RadioGroup
                aria-labelledby="multi-choice-radio-group"
                name="multi-choice-question"
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
        </FormControl>
    );
}
