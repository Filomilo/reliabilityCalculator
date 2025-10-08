import { ref, type Ref } from "vue";
  import { loadScript } from "vue-plugin-load-script";
  import pythonCode from "@/pythonSrc/RelCalcualtor.py?raw";
  declare function loadPyodide(options?: any): Promise<any>;
  declare function loadPyodide(options?: any): Promise<any>;

  class PyoideModule {
  public isInitialized: Ref<boolean>=ref(false);
  private pyodide: any = null;

  public async initialize() {
    if (this.isInitialized.value) return;
      await loadScript("https://cdn.jsdelivr.net/pyodide/v0.28.1/full/pyodide.js")
        if (typeof loadPyodide !== 'function') {
    throw new Error('loadPyodide not found after script load');
  }
    this.pyodide = await loadPyodide();
    console.log("Pyodide loaded");
  //  console.log("Python code length:", pythonCode);

       this.pyodide.FS.writeFile("RelCalcualtor.py", pythonCode);


    this.isInitialized.value = true;
  }

  public getPyodide() {
    if (!this.isInitialized.value) {
      throw new Error("Pyodide is not initialized. Call initialize() first.");
    }
    return this.pyodide;
  }

}



export const pyodideModule = new PyoideModule();
