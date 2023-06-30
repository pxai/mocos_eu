import React from "react"
import { Button } from "@material-ui/core"
import SimpleTabs from "./cp0";

export default function Home() {
  return <div>
    <SimpleTabs />
    <div>Hello world!</div>
    <Button variant="contained" color="primary">
  Primary
</Button>
    </div>
}
