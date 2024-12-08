import './app/global.css';
import { ThemeProvider } from "@/components/theme-provider"
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Page from './app/dashboard/page'; // Import Page component

function App() {
  return (
    // <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
    <>
       <Router>
        <Routes>
          <Route path="/" element={<Page />} />
        </Routes>
      </Router>
    </>
    // </ThemeProvider>
  )
}

export default App;
