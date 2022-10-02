import * as React from "react";
// import Box from '@mui/material/Box';
import Card from "@mui/material/Card";
import Typography from "@mui/material/Typography";

export default function PointDisplay({ points }) {
    return (
        <Card sx={{ textAlign: "center", padding: 2 }}>
            <Typography variant="h5" component="h3">
                Total points: {points}
            </Typography>
        </Card>
    );
}
