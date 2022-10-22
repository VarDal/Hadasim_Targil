import {
  Button,
  Container,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  IconButton,
  List,
  ListItem,
  ListItemButton,
  TextField,
  Typography,
} from "@mui/material";
import React, { useEffect, useState } from "react";
import axios from "axios";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import DeleteIcon from "@mui/icons-material/Delete";

const url = "http://127.0.0.1:8000/";

function App() {
  const [hospitalMembers, setHospitalMembers] = useState([]);
  const [open, setOpen] = React.useState(false);
  const [name, setName] = React.useState("");
  const [isEdit, setIsEdit] = React.useState(false);
  const [clickedMember, setClickedMember] = React.useState(null);

  const handleChange = (event) => {
    setName(event.target.value);
  };
  const handleClickOpen = () => {
    setIsEdit(false);
    setOpen(true);
  };

  const handleClose = () => {
    setName("");
    setOpen(false);
    setClickedMember(null);
  };
  const getAllHospitalMembers = async () => {
    const hospitalMembers = await axios.get(url);
    setHospitalMembers(hospitalMembers.data);
  };

  const addHospitalMember = async () => {
    const hospitalMember = await axios.post(url, {
      name,
    });
    setHospitalMembers((prevState) => {
      const clonePrevState = [...prevState];
      clonePrevState.push(hospitalMember.data);
      return clonePrevState;
    });
    handleClose();
  };

  const deleteHospitalMember = async (id) => {
    const hospitalMember = await axios.delete(url + id);
    setHospitalMembers((prevState) => {
      const clonePrevState = [...prevState];
      const deleteIndex = clonePrevState.findIndex(
        (hospitalMember) => hospitalMember.id === id
      );
      clonePrevState.splice(deleteIndex, 1);
      return clonePrevState;
    });
  };

  const updateHospitalMember = async () => {
    const hospitalMember = await axios.put(url + clickedMember.id, {
      name,
    });
    setHospitalMembers((prevState) => {
      const clonePrevState = [...prevState];
      const updateIndex = clonePrevState.findIndex(
        (hospitalMember) => hospitalMember.id === clickedMember.id
      );
      clonePrevState[updateIndex] = {
        ...clickedMember,
        name,
      };
      return clonePrevState;
    });
    handleClose();
  };

  const handleUpdateMember = (hospitalMember) => {
    setIsEdit(true);
    setClickedMember(hospitalMember);
    setName(hospitalMember.name);
    setOpen(true);
  };

  useEffect(() => {
    getAllHospitalMembers();
  }, []);

  return (
    <Container>
      <List>
        {hospitalMembers.map((hospitalMember) => (
          <ListItemButton
            key={hospitalMember.id}
            onClick={() => handleUpdateMember(hospitalMember)}
          >
            <ListItem
              secondaryAction={
                <IconButton
                  onClick={(e) => {
                    e.stopPropagation();
                    deleteHospitalMember(hospitalMember.id);
                  }}
                  edge="end"
                  aria-label="delete"
                >
                  <DeleteIcon />
                </IconButton>
              }
            >
              {hospitalMember.name}
            </ListItem>
          </ListItemButton>
        ))}
      </List>
      <Fab onClick={handleClickOpen} color="primary" aria-label="add">
        <AddIcon />
      </Fab>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>
          {isEdit ? "Update Hospital member" : "Add New Hospital member"}
        </DialogTitle>
        <DialogContent>
          <TextField
            onChange={handleChange}
            autoFocus
            margin="dense"
            id="name"
            label="name"
            fullWidth
            variant="standard"
            value={name}
          />
          {isEdit && (
            <>
              <Typography>
                sick date: {clickedMember?.sickDate || "No Date"}
              </Typography>
              <Typography>
                recovery date: {clickedMember?.recoveryDate || "No Date"}
              </Typography>
              <Typography>
                vaccine date: {clickedMember?.vaccineDate || "No Date"}
              </Typography>
            </>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button
            variant="contained"
            onClick={!isEdit ? addHospitalMember : updateHospitalMember}
          >
            {!isEdit ? "Add" : "Update"}
          </Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
}

export default App;
