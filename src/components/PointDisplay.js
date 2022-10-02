import * as React from "react";
// import Box from '@mui/material/Box';
import Card from "@mui/material/Card";

export default function PointDisplay({ points }) {
    return <Card variant="outlined">{points}</Card>;
}
