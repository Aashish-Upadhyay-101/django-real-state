import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Footer from "./components/Footer";
import Header from "./components/Header";
import NotFound from "./components/NotFound";
import HomePage from "./pages/HomePage";
import ActivatePage from "./pages/ActivatePage";
import LoginPage from "./pages/LoginPage";
import PropertiesPage from "./pages/PropertiesPage";
import RegisterPage from "./pages/RegisterPage";
import { useEffect } from "react";

function App() {
  useEffect(() => {
    toast(
      "This application is mainly focused on backend side, so frontend part is quite incomplete and not all the features and pages are added!",
      {
        position: "top-right",
        autoClose: false,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      }
    );
  }, []);
  return (
    <>
      <Router>
        <Header />
        <main className="py-3">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/properties" element={<PropertiesPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/activate/:uid/:token" element={<ActivatePage />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
          <ToastContainer theme="dark" />
        </main>
        <Footer />
      </Router>
    </>
  );
}

export default App;
