import React from 'react';
import { BarChart, Bar, XAxis, YAxis, ReferenceLine, LabelList } from 'recharts';

const data = [
  { month: 'Jan', PL: 7.8, PY: 18.1 },
  { month: 'Feb', PL: -0.8, PY: -24.2 },
  { month: 'Mar', PL: 3.8, PY: 23.0 },
  { month: 'Apr', PL: -2.8, PY: -22.9 },
  { month: 'May', PL: -4.0, PY: -3.9 },
  { month: 'Jun', PL: 7.5, PY: -9.9 },
  { month: 'Jul', PL: -0.6, PY: -4.4 },
  { month: 'Aug', PL: 0.0, PY: -21.6 },
  { month: 'Sep', PL: 0.6, PY: 32.3 },
  { month: 'Oct', PL: 13.5, PY: 6.2 },
  { month: 'Nov', PL: -2.5, PY: 16.8 },
];

const CustomLabel = (props) => {
  const { x, y, width, value } = props;
  return (
    <text x={x + width / 2} y={y} fill="#000" textAnchor="middle" dy={-6}>
      {`${value > 0 ? '+' : ''}${value}%`}
    </text>
  );
};

const ACPLChart = () => (
  <BarChart width={800} height={400} data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
    <XAxis dataKey="month" />
    <YAxis yAxisId="left" orientation="left" />
    <YAxis yAxisId="right" orientation="right" />
    <ReferenceLine y={0} stroke="#000" />
    <Bar yAxisId="left" dataKey="PL" fill="#82ca9d">
      <LabelList content={<CustomLabel />} />
    </Bar>
    <Bar yAxisId="right" dataKey="PY" fill="#8884d8">
      <LabelList content={<CustomLabel />} />
    </Bar>
  </BarChart>
);

export default ACPLChart;