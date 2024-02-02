import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

const WorkoutPlan = () => {
  const [workoutPlans, setWorkoutPlans] = useState([]);
  const [selectedPlan, setSelectedPlan] = useState({});
  const [trainers, setTrainers] = useState([]);
  const [exercises, setExercises] = useState([]);
  const [selectedTrainer, setSelectedTrainer] = useState('');
  const [selectedExercise, setSelectedExercise] = useState('');
  const [time, setTime] = useState('');
  const [day, setDay] = useState(new Date());
  const [selectedMemberId] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [trainerResponse, exerciseResponse] = await Promise.all([
          axios.get('http://localhost:5000/trainers'),
          axios.get('http://localhost:5000/exercises'),
        ]);

        setTrainers(trainerResponse.data);
        setExercises(exerciseResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    const fetchWorkoutPlans = async () => {
      try {
        const response = await axios.get('http://localhost:5000/workout-plans');
        setWorkoutPlans(response.data);
      } catch (error) {
        console.error('Error fetching workout plans:', error);
      }
    };

    fetchWorkoutPlans();
  }, []);

  const handlePlanSelect = (plan) => {
    setSelectedPlan(plan);
    setTime(plan.time);
    setDay(new Date(plan.day));
  };

  const handleSave = async () => {
    try {
      const requestData = {
        member_name: selectedMemberId,
        trainer_id: selectedTrainer,
        exercise_id: selectedExercise,
        time,
        day,
      };

      if (selectedPlan.id) {
        await axios.put(`http://localhost:5000/workout-plans/${selectedPlan.id}`, requestData);
      } else {
        await axios.post('http://localhost:5000/workout-plans', requestData);
      }

      const response = await axios.get('http://localhost:5000/workout-plans');
      setWorkoutPlans(response.data);

      setSelectedPlan({});
      setSelectedTrainer('');
      setSelectedExercise('');
      setTime('');
      setDay(new Date());
    } catch (error) {
      console.error('Error saving workout plan:', error);
    }
  };

  const handleDelete = async () => {
    try {
      if (selectedPlan.id) {
        await axios.delete(`http://localhost:5000/workout-plans/${selectedPlan.id}`);
        const response = await axios.get('http://localhost:5000/workout-plans');
        setWorkoutPlans(response.data);

        setSelectedPlan({});
        setSelectedTrainer('');
        setSelectedExercise('');
        setTime('');
        setDay(new Date());
      }
    } catch (error) {
      console.error('Error deleting workout plan:', error);
    }
  };

  return (
    <div className="max-w-2xl mx-auto mt-8">
      <h2 className="text-3xl font-bold mb-4">Workout Plans</h2>
      <table className="w-full border-collapse border border-gray-300">
        <thead>
          <tr>
            <th className="py-2 px-4 border-b">Trainer</th>
            <th className="py-2 px-4 border-b">Exercise</th>
            <th className="py-2 px-4 border-b">Time</th>
            <th className="py-2 px-4 border-b">Day</th>
            <th className="py-2 px-4 border-b">Actions</th>
          </tr>
        </thead>
        <tbody>
          {workoutPlans.map((plan) => (
            <tr key={plan.id} className="text-center">
              <td className="py-2 px-4 border-b">{plan.trainer_id}</td>
              <td className="py-2 px-4 border-b">{plan.exercise_id}</td>
              <td className="py-2 px-4 border-b">{plan.time}</td>
              <td className="py-2 px-4 border-b">{plan.day}</td>
              <td className="py-2 px-4 border-b">
                <button
                  className="bg-blue-500 text-white px-3 py-1 rounded mr-2"
                  onClick={() => handlePlanSelect(plan)}
                >
                  Edit
                </button>
                <button
                  className="bg-red-500 text-white px-3 py-1 rounded"
                  onClick={handleDelete}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2 className="text-3xl font-bold mt-8 mb-4">Workout Plan Details</h2>
      <div className="flex flex-col space-y-4">
        <label className="flex flex-col">
          Trainer:
          <select
            value={selectedTrainer}
            onChange={(e) => setSelectedTrainer(e.target.value)}
            className="py-2 px-4 mt-2 border border-gray-300 rounded"
          >
            <option value="">Select Trainer</option>
            {trainers.map((trainer) => (
              <option key={trainer.id} value={trainer.id}>
                {trainer.name}
              </option>
            ))}
          </select>
        </label>

        <label className="flex flex-col">
          Exercise:
          <select
            value={selectedExercise}
            onChange={(e) => setSelectedExercise(e.target.value)}
            className="py-2 px-4 mt-2 border border-gray-300 rounded"
          >
            <option value="">Select Exercise</option>
            {exercises.map((exercise) => (
              <option key={exercise.id} value={exercise.id}>
                {exercise.name}
              </option>
            ))}
          </select>
        </label>

        <label className="flex flex-col">
          Time (HH:mm):
          <input
            type="text"
            value={time}
            onChange={(e) => setTime(e.target.value)}
            placeholder="HH:mm"
            pattern="^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
            title="Enter a valid time in HH:mm format"
            className="py-2 px-4 mt-2 border border-gray-300 rounded"
          />
        </label>

        <label className="flex flex-col">
          Day:
          <DatePicker
            selected={day}
            onChange={(date) => setDay(date)}
            className="py-2 px-4 mt-2 border border-gray-300 rounded"
          />
        </label>

        <button
          onClick={handleSave}
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          Save
        </button>
      </div>
    </div>
  );
};

export default WorkoutPlan;
