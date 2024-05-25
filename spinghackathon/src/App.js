import lenntechLogo from './lenntechLogo.png';
import polarixLogo from './polarixLogo.png';
import spingLogo from './spingLogo.png';
import './App.css';
import {useState} from "react";

function App() {
    const [inputText, setInputText] = useState("");
    const [numberOfProducts, setNumberOfProducts] = useState(1);
    const [showInitialOutput, setShowInitialOutput] = useState(true);

    const handleInputChange = (event) => {
        setInputText(event.target.value);
    }

    const handleNumberOfProductChange = (event) => {
        const newValue = event.target.value;
        if(newValue < 1)
            setNumberOfProducts(1);
        else
            setNumberOfProducts(newValue)
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        setShowInitialOutput(false);
        alert(inputText + "\n" + numberOfProducts);
        console.log(inputText);
    }

    const handleRefresh = (event) => {
        setShowInitialOutput(true);
    }

  return(
      <main className="fullPage">
          <title>Home Page</title>
          <div className="menuBar">
              <h1>Welcome to</h1>
              <img src={lenntechLogo} alt="Lenntech logo" className="lenntechLogo"/>
          </div>
          <div className="appPage">
              <div className="leftColumn">
                  <div>Please add your request below:</div>
                  <textarea
                      placeholder="Input your request here..."
                      className="inputBox"
                      value={inputText}
                      onChange={handleInputChange}
                  />
                  <div className="textAndInputProducts">
                      Number of desired products:
                      <input
                          type="number"
                          defaultValue={1}
                          value={numberOfProducts}
                          onChange={handleNumberOfProductChange}
                          className="inputProducts"
                      />
                  </div>
                  <button className="submitButton" onClick={handleSubmit}>
                      Submit request
                  </button>
              </div>
              <div className="rightColumn">
                  { showInitialOutput ?
                      (
                          <>
                            <div>The best products will appear here once you click "Submit request".</div>
                            <div>For better results, we recommend to request at least 3 products.</div>
                          </>
                      ) : (
                          <div>muie</div>
                      )
                  }
              </div>
          </div>
          <div className="bottomPage">
              <div>Solution developed by:</div>
              <a href="https://www.lenntech.com/">
                <img src={lenntechLogo} alt="Lenntech logo" className="bottomImages"/>
              </a>
              <a href="https://polarixdata.com/en/">
                <img src={polarixLogo} alt="Polarix logo" className="bottomImages"/>
              </a>
              <a href="https://sping.nl/">
                <img src={spingLogo} alt="Sping logo" className="bottomImages"/>
              </a>
          </div>
      </main>
  );
}

export default App;
