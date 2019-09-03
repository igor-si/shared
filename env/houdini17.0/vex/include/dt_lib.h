// Calculates dot product between two quaternions
float QDot(vector4 q1; vector4 q2)
{
	return q1.w*q2.w+q1.x*q2.x+q1.y*q2.y+q1.z*q2.z;
}

