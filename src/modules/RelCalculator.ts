import { pyodideModule } from "./pyodide"


const runCalcualtion=(timings: any, numberOfElements: number, functionName: String): any=>{
  pyodideModule.getPyodide().globals.set("timings",  pyodideModule.getPyodide().toPy(timings));
  pyodideModule.getPyodide().globals.set("numberOfElements", pyodideModule.getPyodide().toPy(numberOfElements));
const result=pyodideModule.getPyodide().runPython(`
from RelCalcualtor import dystrybunataFt,funkcjaNiezawdnosciRt,funkcjaGestaft,funkcjaIntensywnoscilambdat,rozkladTrwalosciEta
int_map = {int(k): int(v) for k, v in timings.items()}
result=${functionName}(int_map, numberOfElements)
print(result)
result
`);
let formattedReuslt=null
  if(result.toJs!==undefined){
   formattedReuslt= result.toJs({dict_converter : Object.fromEntries})
   result.destroy();}
  else
    formattedReuslt= result
console.log(formattedReuslt)
return formattedReuslt
}


export const dystrybunataFt=(timings: any, numberOfElements: number): any => {
return runCalcualtion(timings,numberOfElements,"dystrybunataFt")
}

export const funkcjaNiezawdnosciRt=(timings: any, numberOfElements: number): any => {
return runCalcualtion(timings,numberOfElements,"funkcjaNiezawdnosciRt")
}

export const funkcjaGestaft=(timings: any, numberOfElements: number): any => {
return runCalcualtion(timings,numberOfElements,"funkcjaGestaft")
}

export const funkcjaIntensywnoscilambdat=(timings: any, numberOfElements: number): any => {
return runCalcualtion(timings,numberOfElements,"funkcjaIntensywnoscilambdat")
}

export const rozkladTrwalosciEta=(timings: any, numberOfElements: number): any => {
return runCalcualtion(timings,numberOfElements,"rozkladTrwalosciEta")
}
// dystrybunataFt(timings, numberOfElements)
