import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Main from './components/Main';
import Detail from './components/Detail';

function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    <Route path="/" element={<Main />} />
                    <Route path="/detail/:id" element={<Detail />} />
                </Routes>
            </Router>
        </div>
    );
}

export default App;
